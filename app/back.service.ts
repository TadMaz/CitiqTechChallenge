import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BackService {

  host: string = "localhost:8000/";

  constructor(private http: HttpClient) { }

  get(url: string, params: object){
    
    return this.http.get(this.host.concat(url), params=params);
  }

  post(url:string, params: object){
    return this.http.post(this.host.concat(url), params);
  }
}
