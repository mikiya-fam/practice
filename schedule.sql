CREATE TABLE T_SCHEDULE(
    schedule_id int not null primary key,
    start_date timestamp,
    end_date timestamp,
    event_name varchar(20),
    place varchar(20),
    comment varchar(500),
    member_id int,
    member_count int,
    create_date timestamp default current_timestamp,
    update_date timestamp default current_timestamp,
    delete_flag char(1)
);