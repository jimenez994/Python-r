SELECT users2.id, users2.first_name as friend_first_name, users2.last_name as friend_last_name, users.id, users.first_name, users.last_name
FROM users
    LEFT JOIN friendships ON  users.id = friendships.users_id
    LEFT JOIN users as users2 ON users2.id = friendships.users_id1 
;