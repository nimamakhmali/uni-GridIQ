-- Users
CREATE TABLE IF NOT EXISTS users (
    user_id        SERIAL PRIMARY KEY,
    username       VARCHAR(50) NOT NULL UNIQUE,
    password_hash  VARCHAR(255) NOT NULL,
    role           user_role_enum NOT NULL,
    created_at     TIMESTAMP NOT NULL DEFAULT NOW()
);


