from flask_restplus import Resource

from api.models import AssetCategory
from . import api
from api.middlewares.token_required import token_required


@api.route('/asset-categories/stats')
class AssetCategoryCount(Resource):
    """
    Resource class for getting asset categories and
    their corresponding asset counts
    """

    @token_required
    def get(self):
        """
        Get method for asset categories and corresponding asset count

        :return: asset categories and counts
        """

        asset_categories = AssetCategory._query().all()
        data = []
        for asset_category in asset_categories:
            data.append({
                'name': asset_category.name,
                'asset_count': len(asset_category.assets)
            })
        return {
            'message': 'Success',
            'data': data
        }
