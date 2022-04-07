import db_query
nesne = db_query.Query()

advisoor_list = nesne.advisor_query()
print(len(advisoor_list))
print(advisoor_list[1]["registrationID"])
