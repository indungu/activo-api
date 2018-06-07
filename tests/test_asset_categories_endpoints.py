from os import getenv
from flask import json


class TestAssetCategoriesEndpoints:
    def test_asset_categories_stats_endpoint(self, client, new_asset_category, init_db):
        new_asset_category.save()
        response = client.get('/api/v1/asset-categories/stats',
                              headers={'Authorization': getenv('TEST_TOKEN')})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert isinstance(response_json['data'], list)
        assert len(response_json['data']) is not 0
        assert response_json['data'][0]['name'] == 'Laptop'
        new_asset_category.delete()
