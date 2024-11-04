import { HttpClient } from "@angular/common/http";
import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, FormBuilder, Validators } from "@angular/forms";
import { UserInterface } from "../user.interface";
import { Router } from "@angular/router";
import { AuthService } from "../auth.service";
import { environment } from "../environment";

@Component({
    selector: "app-login",
    templateUrl: "./login.component.html",
    standalone: true,
    imports: [ReactiveFormsModule],
})
export class LoginComponent {
    fb = inject(FormBuilder);
    http = inject(HttpClient);
    authService = inject(AuthService);
    router = inject(Router);

    form = this.fb.nonNullable.group({
        email: ["", Validators.required],
        password: ["", Validators.required]
    });

    onSubmit(): void {
        this.http.post<{user: UserInterface}>(
            environment.apiUrl + "/api/login", {
                user: this.form.getRawValue()
            }
        ).subscribe({
            next: (response) => {
            localStorage.setItem("token", response.user.token);
            this.authService.currentUserSig.set(response.user);
            this.router.navigateByUrl("/");
            }, 
            error: response =>{
                alert(response.error);
            }
        });
    }
}