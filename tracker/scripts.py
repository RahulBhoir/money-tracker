from .models import *
from .constants import * 

# to insert data into the models --> Tag, CategoryType, SpendType, 
def insert_data_into_model_using_list(model_name, data):
    for item in data:
        model_name.objects.create(name=item)


# to insert data into the model --> Category
def insert_data_into_model_using_dict(model_name, data):
    for item in data:
        cat_type_id = CategoryType.objects.get(id=item['CAT_TYPE_ID'])
        model_name.objects.create(name=item['CAT_NAME'], category_type=cat_type_id)


# insert data in all models in one go
def call_function():
    insert_data_into_model_using_list(Tag, TAG_MODEL_DATA)
    insert_data_into_model_using_list(SpendType, SPEND_TYPE_MODEL_DATA)
    insert_data_into_model_using_list(CategoryType, CATEGORY_TYPE_MODEL_DATA)
    insert_data_into_model_using_dict(Category, CATEGORY_MODEL_DATA)
    return "Success"
