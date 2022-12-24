statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):
    online_users = []
    for key, value in statuses.items():
        if (value == 'online'):
            online_users.append(key)
    return len(online_users)
        

print(online_count(statuses))

# # long version
# def online_count(people):
#     count = 0
#     for person, status in people.items():
#         if status == "online":
#             count += 1
#     return count

# # short version
# def online_count(people):
#     return len([p for p in people if people[p] == "online"])