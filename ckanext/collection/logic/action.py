import ckan.logic as logic
import ckan.plugins.toolkit as toolkit
from pylons import config

get_action = logic.get_action

@toolkit.side_effect_free
def api_collection_show(context, data_dict):
    data_dict = {
        'include_extras': False,
        'include_datasets': False,
        'include_dataset_count': True,
        'include_users': False,
        'include_groups': False,
        'include_followers': False,
        'include_tags': False,
        'id': config.get('ckanext.collection.api_collection_name_or_id')
    }
    return get_action('group_show')(context, data_dict)
