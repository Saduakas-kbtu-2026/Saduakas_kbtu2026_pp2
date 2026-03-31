-- =========================================================
-- PhoneBook SQL: Functions
-- =========================================================

-- ----------------------------
-- 1. Table Creation
-- ----------------------------
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);

-- =========================================================
-- FUNCTIONS
-- =========================================================

-- Function: Search by pattern (name or phone)
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phone
    FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Function: Get contacts with pagination (LIMIT + OFFSET)
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phone
    FROM phonebook
    ORDER BY id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- =========================================================
-- Usage Examples:
-- Functions:
--   SELECT * FROM search_contacts('Alex');
--   SELECT * FROM get_contacts_paginated(5,0);
-- =========================================================
