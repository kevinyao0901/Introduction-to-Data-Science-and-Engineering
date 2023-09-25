import re

def validate_id_card(id_card):
    pattern = r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|30|31)\d{3}(\d|X)$'
    match = re.match(pattern, id_card)

    if match:
        return True
    else:
        return False

id_card_number = input("请输入身份证号码：")
is_valid = validate_id_card(id_card_number)

if is_valid:
    print("身份证号码合法")
else:
    print("身份证号码不合法")
