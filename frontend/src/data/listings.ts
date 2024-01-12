import __stayListing from "./jsons/__stayListing.json";
import __experiencesListing from "./jsons/__experiencesListing.json";
import { ExperiencesDataType, StayDataType, Hotel } from "./types";


const DEMO_STAY_LISTINGS = __stayListing.map((post, index): Hotel => {
  return {
    ...post,
  };
});

const DEMO_EXPERIENCES_LISTINGS = __experiencesListing.map(
  (post, index): ExperiencesDataType => {
    return {
      ...post,
    };
  }
);

export { DEMO_STAY_LISTINGS, DEMO_EXPERIENCES_LISTINGS };
