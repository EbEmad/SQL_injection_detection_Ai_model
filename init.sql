create table if not exists requests(
    id int auto_increment primary key,
    source_ip varchar(50) not null,
    request_type varchar(50) not null,
    endpoint varchar(255) not null,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    response_time float not null,
    user_agent text,
    content_length int,
    status_code int,
    referrer text,
    query_parameters text,
    headers text,
    error_message text,
    api_version varchar(50),
    client_id VARCHAR(255),
    request_id VARCHAR(255)
);