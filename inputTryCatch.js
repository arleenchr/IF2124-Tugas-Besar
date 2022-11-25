function debug(a){
    try {
        throw alert("Sorry")
    } catch(a) {
        alert("Error!");
    } finally {
        alert("True, it's" + a)
    }
}