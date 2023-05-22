var app = angular.module('mathApp', []);

app.controller('mathController', function($scope, $http, $httpParamSerializerJQLike) {
    $scope.submitForm = function() {
        var data = {
            num1: $scope.num1,
            num2: $scope.num2
        };
        var url = '/' + $scope.operation;
        $http.post(url, $httpParamSerializerJQLike(data), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).then(function(response) {
            if ('result' in response.data) {
                $scope.result = response.data.result;
                $scope.error = '';
            } else {
                $scope.error = response.data.error;
                $scope.result = '';
            }
        });
    };
});

