/////////////////////////////////////////////////////////////////////////////////
// harnessFunction functions that modifies the state
/////////////////////////////////////////////////////////////////////////////////
definition harnessFunction(method f) returns bool =
        f.selector == sig:configureAsset(address,address,address).selector;
