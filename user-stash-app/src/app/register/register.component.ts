import { HttpClient } from "@angular/common/http";
import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, FormBuilder, Validators } from "@angular/forms";
import { UserInterface } from "../user.interface";
import { Router } from "@angular/router";
import { environment } from "../environment";
import { AuthService } from "../auth.service";

@Component({
    selector: "app-register",
    templateUrl: "./register.component.html",
    standalone: true,
    imports: [ReactiveFormsModule],
})
export class RegisterComponent {
    fb = inject(FormBuilder);
    http = inject(HttpClient);
    authService = inject(AuthService);
    router = inject(Router);

    form = this.fb.nonNullable.group({
        username: ["", Validators.required],
        email: ["", Validators.required],
        password: ["", Validators.required]
    });

    onSubmit(): void {
        this.http.post<{user: UserInterface}>(
            environment.apiUrl + "/api/users", {
                user: this.form.getRawValue()
            }
        ).subscribe({
            next: (response) => {
                console.log("response", response);
                localStorage.setItem("token", response.user.token);
                this.authService.currentUserSig.set(response.user);
                this.router.navigateByUrl("/");
            },
            error: (response) =>{
            alert(response.error);
            }
        });
    }
}