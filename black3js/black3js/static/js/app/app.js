'use strict';

var Black3js = angular.module("black3js", ["ui.bootstrap", "ngCookies", "ngGrid"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

Black3js.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})

Black3js.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/feed.html",
            controller: "GameController",
            resolve: {
                games: function (GameService) {
                    return GameService.list();
                }
            }
        })
        .when("/game/:id", {
            templateUrl: "static/js/app/views/view.html",
            controller: "GameController",
            resolve: {
                games: function ($route, GameService) {
                    var game_id = $route.current.params.id
                    return GameService.get(game_id);
                }
            }
        })
        .when("/score/:id", {
            templateUrl: "static/js/app/views/score.html",
            controller: "GameController",
            resolve: {
                games: function ($route, GameService) {
                    var game_id = $route.current.params.id
                    return GameService.get(game_id);
                }
            }
        })
        .otherwise({
            redirectTo: '/'
        })
})