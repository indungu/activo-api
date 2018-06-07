from flask import json, request
import os
from api.models.asset_category import AssetCategory


class TestAssetCategoryEndpoints:
    """
    Tests that a single asset category can be deleted
    """
    def test_delete_asset_category(self, client, init_db, auth_headers):
        asset_category = AssetCategory(name='TestLaptop')
        asset_category.save()

        response = client.delete('/api/v1/asset_categories/{}'.format(
          asset_category.id), headers=auth_headers)
          
        response_json = json.loads(response.data.decode('utf-8'))
  
        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert response_json['message'] == 'category deleted successfully'
