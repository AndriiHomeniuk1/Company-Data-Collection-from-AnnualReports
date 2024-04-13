import json


def compare_data(file_name, file2='forbes') -> None:
    new_data = {}
    with open(f'reports/{file2}.json', 'r', encoding='utf-8') as forbes, \
            open(f'reports/{file_name}.json', 'r', encoding='utf-8') as exchange:
        forbes_data = json.load(forbes)
        exchange_data = json.load(exchange)
        for company_forbes in forbes_data:
            for company_exchange in exchange_data:
                if company_forbes["name"] in company_exchange["name"]:
                    new_data[company_forbes["name"]] = {
                        "rank": company_forbes["rank"],
                        "name": company_forbes["name"],
                        "name_v2": company_exchange["name"],
                        "link": company_exchange["link_name"],
                    }

                    break

    print(new_data)
    print(len(new_data))

    with open(f'reports/{file_name}_companies.json', 'w') as file:
        json.dump(new_data, file, indent=4)




file_names = ["aim_companies.json", "amex_companies.json", "asx_companies.json", "lse_companies.json",
              "nasdaq_companies.json", "nyse_companies.json", "otc_companies.json", "tsx_companies.json",
              "tsx_v_companies.json"]


def compare_json_file(files: list):
    all_data = {}

    for file_name in files:
        with open(f'reports/{file_name}', "r") as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                all_data[key] = value


    output_file = "output.json"
    with open(output_file, "w") as json_output:
        json.dump(all_data, json_output, indent=4)



if __name__ == "__main__":
    pass
    # compare_data("tsx_v")
    # compare_json_file(file_names)















