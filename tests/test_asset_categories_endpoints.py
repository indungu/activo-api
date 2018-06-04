from os import getenv
from flask import json


class TestAssetCategoriesEndpoints:
    def test_get_asset_count(self, client, init_db):
        response = client.get('/api/v1/asset-categories/stats',
                              headers={'Authorization': getenv('TEST_TOKEN')})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert response_json['message'] == 'Success'
        assert isinstance(response_json['data'], list)
