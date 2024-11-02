import { CommonModule } from "@angular/common";
import { Component, inject, OnInit } from "@angular/core";
import { RouterOutlet, RouterLink } from "@angular/router";
import { AuthService } from "./services/auth.service";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink],
  templateUrl: "./app.component.html",
})
export class AppComponent implements OnInit {
  authService = inject(AuthService);
  ngOnInit(): void {}

  logout(): void {
    console.log("logout")
  }
}
