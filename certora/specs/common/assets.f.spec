function assetsOne(address asset) returns bool {
    address[] assets = getAssetsList();
    mathint decimals = getAssetDecimals(asset);

    return assets.length == 1
        && assets[0] == asset
        && decimals <= 18
        && decimals >= 6;
}

function assetsZero() returns bool {
    address[] assets = getAssetsList();
    return assets.length == 0;
}
