CREATE TABLE T_MEMBER(
    member_id int not null primary key,
    last_name varchar(10),
    first_name varchar(10),
    sex char(1),
    user_id varchar(10),
    password varchar(10),
    create_date timestamp default current_timestamp,
    update_date timestamp default current_timestamp,
    delete_flag char(1)
);