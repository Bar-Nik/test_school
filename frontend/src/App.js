import ApiManager from  "./Managers/ApiManager"
import UserManager from "./Managers/UserManager";

export default function App()
{
    this.ApiManager = new ApiManager();
    this.UserManager = new UserManager();
}

App.prototype.Init = function()
{
    console.log("App init");
    this.ApiManager.GetTestResponse();

}