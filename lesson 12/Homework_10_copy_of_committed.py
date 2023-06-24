import csv


def open_csv_file_dict(tech_inventory, to_print=True) -> list:
    """
    :param tech_inventory: file path
    :param to_print: flag=  if willing to print
    :return: list of rows,
             every row - dict,
             keys= headers of csv file
    """
    with open(tech_inventory, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        for row in rows:
            print(type(row), row)
    return rows


def generate_csv_rows(all_data) -> tuple:
    # to generate rows and headers in the file
    rows = list()
    header = ["model", "category", "brand", "price"]
    for header in all_data:
        print(type(header), header)
    return rows, header


def create_position_id_index(all_data: list, column_name: str) -> dict:
    """
    :param all_data:
    :param column_name:
    :return: index,
    """
    new_index = dict()
    for i, data_entry in enumerate(all_data):
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(i)
    return new_index


def create_subindex_brand(all_data):
    # list of all brands
    brand_list = set((x['brand'] for x in all_data))
    index_1 = dict()
    # for each brand:
    # get the list of all ids of products with that brand
    # and return them in a dictionary
    for brand in brand_list:
        index_1[brand] = tuple(x["brand"] for x in tech_data if x['brand'])
    return index_1


def create_subindex_category(all_data):
    # list of all categories
    category_list = set((x['category'] for x in all_data))
    index_2 = dict()

    # for each (category):
    # get the list of all ids of products with that (category)
    # and return them in a dictionary
    for category in category_list:
        index_2[category] = tuple(x["category"] for x in tech_data if x['category'])
    return index_2


if __name__ == '__main__':
    tech_data = open_csv_file_dict('tech_inventory.csv', to_print=True)

    generated_rows, generated_header = generate_csv_rows(tech_data)
    open_csv_file_dict('tech_inventory.csv', generated_header)

    model_index = create_position_id_index(tech_data, "model")
    print(type(model_index), model_index)

    category_index = create_position_id_index(tech_data, "category")
    print(type(category_index), category_index)

    brand_index = create_position_id_index(tech_data, "brand")
    print(type(brand_index), brand_index)

    price_index = create_position_id_index(tech_data, "price")
    print(type(price_index), price_index)

    category_subindex = create_subindex_category(tech_data)
    print(type(category_subindex), category_subindex)

    brand_subindex = create_subindex_brand(tech_data)
    print(type(brand_subindex), brand_subindex)
    brands = ((b, len(brand_subindex[b])) for b in brand_subindex.keys())
    for b in brands:
        print(f'{b[0]}: {b[1]}')
