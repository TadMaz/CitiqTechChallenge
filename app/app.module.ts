import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PostComponent } from './post/post.component';
import { ContentComponent } from './content/content.component';
import { MenuComponent } from './menu/menu.component';
import { Routes, RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { LogComponent } from './log/log.component';


const appRoutes: Routes = [
  {path: 'login', component: LogComponent},
  {path: '', component: LogComponent,},
  {path:'home', component: ContentComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    PostComponent,
    ContentComponent,
    MenuComponent,
    LogComponent,
    LogComponent
  ],
  imports: [
    RouterModule.forRoot(
      appRoutes,
    ),
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
