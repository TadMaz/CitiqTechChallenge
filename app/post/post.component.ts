import { Component, OnInit } from '@angular/core';
import { BackService } from '../back.service';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

  public title: string;
  public body: string;
  public votes: number;

  constructor(private backService: BackService) { }

  ngOnInit() {;
  
    this.title = "Title";
    this.body = "This a body";
    this.votes = 10;

  }

  voteUp(): void{
    const params = {};
    this.backService.post("/vote", params)
      .subscribe(
        res => {
          this.votes = res['votes'];
        }
      )
  }


  voteDown(): void{
    const params = {};
    this.backService.post("/vote", params)
      .subscribe(
        res => {
          this.votes = res['votes'];
        }
      )
  }
}
