// Creating the module
var app = angular.module('myApp', ['ngRoute']);

// Configuring the routes
app.config(function($routeProvider) {
    $routeProvider
    .when('/', {
        templateUrl : 'templates/home.html',
        controller : 'homeCtrl'
    })
    .when('/add', {
        templateUrl : 'templates/add.html',
        controller : 'addCtrl'
    })
    .when('/subtract', {
        templateUrl : 'templates/subtract.html',
        controller : 'subtractCtrl'
    })
    .when('/multiply', {
        templateUrl : 'templates/multiply.html',
        controller : 'multiplyCtrl'
    })
    .when('/divide', {
        templateUrl : 'templates/divide.html',
        controller : 'divideCtrl'
    });
});

// Creating the controllers
app.controller('homeCtrl', function($scope) {
    $scope.message = 'Welcome to the Mathematical Operations Webapp!';
});

app.controller('addCtrl', function($scope, $http) {
    $scope.add = function() {
        var num1 = $scope.num1;
        var num2 = $scope.num2;
        $http.post('/add', {num1: num1, num2: num2}).then(function(response) {
            $scope.result = response.data.result;
        });
    };
});

app.controller('subtractCtrl', function($scope, $http) {
    $scope.subtract = function() {
        var num1 = $scope.num1;
        var num2 = $scope.num2;
        $http.post('/subtract', {num1: num1, num2: num2}).then(function(response) {
            $scope.result = response.data.result;
        });
    };
});

app.controller('multiplyCtrl', function($scope, $http) {
    $scope.multiply = function() {
        var num1 = $scope.num1;
        var num2 = $scope.num2;
        $http.post('/multiply', {num1: num1, num2: num2}).then(function(response) {
            $scope.result = response.data.result;
        });
    };
});

app.controller('divideCtrl', function($scope, $http) {
    $scope.divide = function() {
        var num1 = $scope.num1;
        var num2 = $scope.num2;
        $http.post('/divide', {num1: num1, num2: num2}).then(function(response) {
            $scope.result = response.data.result;
        });
    };
});