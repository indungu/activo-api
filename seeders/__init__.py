from api.models import AssetCategory, Asset, Attribute


def seed_asset_category():
    apple_tv = AssetCategory(name='Apple TV')
    apple_tv_assets = [
        Asset(tag='AND/345/EWR', serial='GRGR334TG'),
        Asset(tag='AND/654/FWE', serial='SDW435OOJ'),
        Asset(tag='AND/234/FJA', serial='JHDHG23JJ'),
        Asset(tag='AND/345/AFW', serial='AFWEF34OF')
    ]
    for asset in apple_tv_assets:
        apple_tv.assets.append(asset)
    apple_tv_attributes = [
        Attribute(label='warranty', is_required=False,
                  input_control='text-area', choices='multiple choices'),
        Attribute(label='size', is_required=False,
                  input_control='text-area', choices='multiple choices')
    ]
    for attribute in apple_tv_attributes:
        apple_tv.attributes.append(attribute)
    apple_tv.save()

    laptops = AssetCategory(name='Laptops')
    laptops.save()

    usb_dongles = AssetCategory(name='USB Dongles')
    usb_dongles_attributes = [
        Attribute(label='color', is_required=False,
                  input_control='text-area', choices='multiple choices'),
        Attribute(label='length', is_required=False,
                  input_control='text-area', choices='multiple choices')
    ]
    for attribute in usb_dongles_attributes:
        usb_dongles.attributes.append(attribute)
    usb_dongles.save()

    chromebooks = AssetCategory(name='ChromeBooks')
    chromebooks_assets = [
        Asset(tag='AND/3235/ERR', serial='NBA220FWE'),
        Asset(tag='AND/634/FHE', serial='NTW456RGR'),
        Asset(tag='AND/246/TRA', serial='JAA556EGR'),
        Asset(tag='AND/875/HJR', serial='AWF232EGG')
    ]
    for asset in chromebooks_assets:
        chromebooks.assets.append(asset)
    chromebooks.save()

    chairs = AssetCategory(name='chairs')
    chairs_attributes = [
        Attribute(label='type', is_required=True,
                  input_control='input-field', choices='multiple choices')
    ]
    for attribute in chairs_attributes:
        chairs.attributes.append(attribute)
    chairs.save()
