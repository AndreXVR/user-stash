import { CommonModule } from "@angular/common";
import { Component, OnInit } from "@angular/core";
import { RouterOutlet, RouterLink } from "@angular/router";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink],
  templateUrl: "./app.component.html",
})
export class AppComponent implements OnInit {
  ngOnInit(): void {}

  logout(): void {
    console.log("logout")
  }
}
