from flask_restplus import Resource

from api.models import AssetCategory
from main import api
from api.middlewares.token_required import token_required


@api.route('/asset-categories/stats')
class AssetCategoryStats(Resource):
    """
    Resource class for getting asset categories and
    their corresponding asset counts
    """

    @token_required
    def get(self):
        """
        Gets asset categories and the corresponding asset count
        """

        asset_categories = AssetCategory._query().all()
        data = []
        for asset_category in asset_categories:
            data.append({
                'id': asset_category.id,
                'name': asset_category.name,
                'asset_count': asset_category.assets_count
            })
        return {
            'status': 'success',
            'data': data
        }
        

@api.route('/asset_categories/<string:id>')
class AssetCategoryResource(Resource):
    """
    include a docstring explaining what this view does
    """
    @token_required
    def delete(self, id):
        single_category = AssetCategory.get(id)
        if not single_category:
            raise ValidationError(dict(message='Asset category not found'), 404)

        single_category.delete()

        return {
            'status': 'success',
            'message': 'category deleted successfully'
        }, 200

