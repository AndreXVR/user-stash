import { CommonModule } from "@angular/common";
import { Component, inject, OnInit } from "@angular/core";
import { RouterOutlet, RouterLink } from "@angular/router";
import { HttpClient } from "@angular/common/http";
import { UserInterface } from "./user.interface";
import { AuthService } from "./auth.service";
import { environment } from "./environment";

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
    this.http.get<{user: UserInterface}>(environment.apiUrl + "/api/user").subscribe({
      next: (response) => {
        this.authService.currentUserSig.set(response.user);
      },
      error: () => {
        this.authService.currentUserSig.set(null);
      }
    })
  }

  logout(): void {
    localStorage.setItem("token", "")
    this.authService.currentUserSig.set(null);
  }
}
