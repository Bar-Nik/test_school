export default function ApiManager()
{
    this.host = "127.0.0.1";
    this.port = "6000";
    this.apiAddr = `http://${this.host}:${this.port}`;
}

ApiManager.prototype.GetTestResponse = async function () {
    let response = await fetch(this.apiAddr, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    });
    console.log(response);
}