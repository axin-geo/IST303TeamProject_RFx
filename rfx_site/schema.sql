DROP TABLE IF EXISTS rfx_owner_tbl;

CREATE TABLE rfx_owner_tbl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rfx_name TEXT NOT NULL,
    owner_name TEXT NOT NULL,
    email TEXT NOT NULL,
    team TEXT NOT NULL
);