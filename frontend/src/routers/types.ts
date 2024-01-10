import { ComponentType } from "react";

export interface LocationStates {
  "/"?: {};
  "/#"?: {};
  "/home-2"?: {};
  "/home-3"?: {};
  "/home-1-header-2"?: {};
  //
  "/listing-flights"?: {};
  //
  "/listing-stay"?: {};
  "/hotels/:id"?: {};
  "/listing-stay-detail"?: {};
  //
  "/listing-experiences"?: {};
  "/listing-experiences-detail"?: {};
  //

  //
  "/checkout"?: {};
  "/pay-done"?: {};
  //
  "/account"?: {};
  "/account-password"?: {};
  "/account-billing"?: {};
  //

  //
  "/search"?: {};
  "/about"?: {};
  "/contact"?: {};
  "/login"?: {};
  "/signup"?: {};
  "/forgot-pass"?: {};
  "/page404"?: {};
  "/subscription"?: {};

  "/listing-stay-hanoi"?: {};
  "/listing-stay-tphcm"?: {};
  "/listing-stay-nhatrang"?: {};
  "/listing-stay-danang"?: {};
  "/listing-stay-dalat"?: {};
  "/listing-stay-halong"?: {};
  "/listing-stay-cantho"?: {};
  "/listing-stay-phuquoc"?: {};
  "/listing-stay-vungtau"?: {};
}

export type PathName = keyof LocationStates;

export interface Page {
  path: PathName;
  exact?: boolean;
  component: ComponentType<Object>;
}
