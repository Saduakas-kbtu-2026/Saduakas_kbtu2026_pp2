-- =========================================================
-- PhoneBook SQL: Procedures
-- =========================================================

-- =========================================================
-- PROCEDURES
-- =========================================================

-- Procedure: Insert or update a single contact
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- Procedure: Bulk insert from JSON list with phone validation
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(p_data JSON)
LANGUAGE plpgsql
AS $$
DECLARE
    item JSON;
    v_name VARCHAR;
    v_phone VARCHAR;
BEGIN
    FOR item IN SELECT * FROM json_array_elements(p_data)
    LOOP
        v_name := item->>'name';
        v_phone := item->>'phone';

        -- Validate phone: digits only, optional leading +
        IF v_phone ~ '^\+?\d{7,15}$' THEN
            PERFORM upsert_contact(v_name, v_phone);
        ELSE
            RAISE NOTICE 'Invalid phone: % for %', v_phone, v_name;
        END IF;
    END LOOP;
END;
$$;

-- Procedure: Delete by name or phone
CREATE OR REPLACE PROCEDURE delete_contact_by(p_type VARCHAR, p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_type = 'name' THEN
        DELETE FROM phonebook WHERE name = p_value;
    ELSIF p_type = 'phone' THEN
        DELETE FROM phonebook WHERE phone = p_value;
    ELSE
        RAISE EXCEPTION 'Invalid type: must be "name" or "phone"';
    END IF;
END;
$$;

-- =========================================================
-- Usage Examples:
-- Procedures:
--   CALL upsert_contact('Alice', '555123456');
--   CALL bulk_insert_contacts('[{"name":"Bob","phone":"1234567890"}]'::json);
--   CALL delete_contact_by('phone','555123456');
-- =========================================================
