import csv
from uuid import uuid4


def open_csv_file_dict(tech_inventory, to_print=False) -> list:
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
            uid = reader.line_num - 1
            print(row)
    return rows


def create_id_index(all_data: list, column_name: str) -> dict:
    """
    :param all_data:
    :param column_name:
    :return: new_index,
    """
    new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(data_entry)
    return new_index


def create_subindex_brand(all_data):
    # list of all brands
    brand_list = set((x['brand'] for x in all_data))
    index_1 = dict()
    # for each brand:
    # get the list of all ids of products with that brand
    # and return them in a dictionary
    for brand in brand_list:
        index_1[brand] = tuple(x["brand"] for x in all_data if x['brand'] == brand)
    return index_1


def create_subindex_category(all_data):
    # list of all categories
    category_list = set((x['category'] for x in all_data))
    index_2 = dict()

    # for each (category):
    # get the list of all ids of products with that (category)
    # and return them in a dictionary
    for category in category_list:
        index_2[category] = tuple(x["category"] for x in all_data if x['category'] == category)
    return index_2


if __name__ == '__main__':
    tech_data = open_csv_file_dict('tech_inventory.csv', to_print=False)

    unique_position_id_index = dict()
    unique_uuid_index = dict()
    for _id, row in enumerate(tech_data):
        unique_position_id_index[_id] = row
        unique_uuid_index[uuid4().int] = row
    print(unique_position_id_index)
    # to print all info on one specific product:
    print(unique_position_id_index[4])
    print('---')

    model_index = create_id_index(tech_data, "model")
    print(model_index)
    print('---')

    category_index = create_id_index(tech_data, "category")
    print(category_index)
    print('---')

    brand_index = create_id_index(tech_data, "brand")
    print(brand_index)
    print('---')

    price_index = create_id_index(tech_data, "price")
    print(price_index)
    print('---')

    category_subindex = create_subindex_category(tech_data)
    print(category_subindex)
    categories = ((c, len(category_subindex[c])) for c in category_subindex.keys())
    for c in categories:
        print(f'{c[0]}: {c[1]}')

    brand_subindex = create_subindex_brand(tech_data)
    print(brand_subindex)
    brands = ((b, len(brand_subindex[b])) for b in brand_subindex.keys())
    for b in brands:
        print(f'{b[0]}: {b[1]}')
