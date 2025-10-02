-- Models
CREATE TABLE IF NOT EXISTS models (
    model_id    SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    version     VARCHAR(20) NOT NULL,
    metrics     JSONB,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (name, version)
);


