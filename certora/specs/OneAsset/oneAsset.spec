function oneAsset(address asset) returns bool {
    address[] assetsList = getAssetsList();
    uint256 decimals = getAssetDecimals(asset);

    return assetsList.length == 1
        && assetsList[0] == asset
        && decimals <= 18
        && decimals >= 6;
}
