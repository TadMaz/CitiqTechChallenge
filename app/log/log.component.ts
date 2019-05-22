import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { BackService } from '../back.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './log.component.html',
  styleUrls: ['./log.component.css'],
})
export class LogComponent implements OnInit {

  loginForm: FormGroup;
  
  constructor(private backService: BackService, private router: Router) { }

  ngOnInit() {
    this.loginForm = new FormGroup({
      username: new FormControl(''),
      password: new FormControl(''),
    })
  }

  // When you submit the form for a login
  onSubmit(){

    const params = this.loginForm.value();
    this.backService.post('login', params)
      .subscribe(
        res=>{
          // if (res["success"] == true) {
          //   this.router.navigate(["home"]);
          // } else {
            // this.wrongLogin();
          // }
        }
      )
  }

  // When you make a wrong login signify it
  wrongLogin(){

  }

}
