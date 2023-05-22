import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  num1: number;
  num2: number;
  result: number;

  constructor(private http: HttpClient) {}

  add() {
    this.http.post('/add', {num1: this.num1, num2: this.num2}).subscribe(data => {
      this.result = data['result'];
    });
  }

  subtract() {
    this.http.post('/subtract', {num1: this.num1, num2: this.num2}).subscribe(data => {
      this.result = data['result'];
    });
  }

  multiply() {
    this.http.post('/multiply', {num1: this.num1, num2: this.num2}).subscribe(data => {
      this.result = data['result'];
    });
  }

  divide() {
    this.http.post('/divide', {num1: this.num1, num2: this.num2}).subscribe(data => {
      this.result = data['result'];
    });
  }
}
