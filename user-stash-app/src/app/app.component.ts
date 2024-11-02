import { CommonModule } from "@angular/common";
import { Component, inject, OnInit } from "@angular/core";
import { RouterOutlet, RouterLink } from "@angular/router";
import { AuthService } from "./auth.service";
import { HttpClient } from "@angular/common/http";
import { environment } from "./environment";
import { UserInterface } from "./user.interface";

@Component({
  selector: "app-root",
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink],
  templateUrl: "./app.component.html",
})
export class AppComponent implements OnInit {
  authService = inject(AuthService);
  http = inject(HttpClient);

  ngOnInit(): void {
    this.http.get<{user: string}>(environment.apiUrl + "/user").subscribe({
      next: (response) => {
        console.log("response", response);
      }
    })
  }

  logout(): void {
    console.log("logout")
  }
}
