export default function ApiManager()
{
    this.host = "127.0.0.1";
    this.port = "8000";
    this.apiAddr = `http://${this.host}:${this.port}/api`;
}

ApiManager.prototype.GetTestResponse = async function() {
    let response = await fetch(this.apiAddr)
    return await response.text();
}