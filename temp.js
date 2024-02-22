// fn to TTC, TTR ,(unix)
// business hours
// json - UTC -> { "sunday": {st: "9:00", end: "13:00"}, "monday":m {}}
// OP - milliseconds
const _map = [
  "sunday",
  "monday",
  "tuesday",
  "wednesday",
  "thursday",
  "friday",
  "saturday",
];
function incidentResolutionPerformance(
  incidentCreatedAt,
  incidentResolvedAt,
  businessHours
) {
  let differenceInMs =
    incidentResolvedAt.getTime() - incidentCreatedAt.getTime();
  if (differenceInMs < 0) {
    throw new Error("Invalid date!");
  }
  let businessHoursInMs = [];
  businessHours.forEach((_, i) => {
    let start = businessHours[i].startTime.split(":");
    let end = businessHours[i].endTime.split(":");
    let startTime = new Date(0).setHours(Number(start[0]), Number(start[1]));
    let endTime = new Date(0).setHours(Number(end[0]), Number(end[1]));
    businessHoursInMs.push(endTime - startTime);
  });
  // console.log(differenceInMs, businessHoursInMs);
  let effectiveTime = 0;
  let currentTimestamp = incidentCreatedAt.getTime();
  while (currentTimestamp < incidentResolvedAt.getTime()) {
    currentTimestamp += 86400000; // 1 Day in ms
    effectiveTime += businessHoursInMs[new Date(currentTimestamp).getDay()];
  }
  // console.log(effectiveTime);

  let start = businessHours[0].startTime.split(":");
  let startTime = new Date(incidentCreatedAt.getTime()).setHours(
    Number(start[0]),
    Number(start[1])
  );
  effectiveTime = effectiveTime - (startTime - incidentCreatedAt.getTime());

  let end = businessHours[6].endTime.split(":");
  let endTime = new Date(incidentResolvedAt.getTime()).setHours(
    Number(end[0]),
    Number(end[1])
  );
  effectiveTime = effectiveTime - (incidentResolvedAt.getTime() - endTime);
  // console.log(differenceInMs, effectiveTime);
  return effectiveTime;
}

const startTime = 1707866700000;
console.log("startTime", new Date(startTime).toLocaleString());
const endTime = 1708151700000;
console.log("endTime", new Date(endTime).toLocaleString());
const businessHours2 = {
  sunday: {
    startTime: "09:00",
    endTime: "13:00",
  },
  monday: {
    startTime: "09:00",
    endTime: "17:00",
  },
  tuesday: {
    startTime: "09:00",
    endTime: "17:00",
  },
  wednesday: {
    startTime: "09:00",
    endTime: "17:00",
  },
  thursday: {
    startTime: "09:00",
    endTime: "17:00",
  },
  friday: {
    startTime: "09:00",
    endTime: "17:00",
  },
  saturday: {
    startTime: "09:00",
    endTime: "17:00",
  },
};
const businessHours = [
  {
    startTime: "09:00",
    endTime: "13:00",
  },
  {
    startTime: "09:00",
    endTime: "17:00",
  },
  {
    startTime: "09:00",
    endTime: "17:00",
  },
  {
    startTime: "09:00",
    endTime: "17:00",
  },
  {
    startTime: "09:00",
    endTime: "17:00",
  },
  {
    startTime: "09:00",
    endTime: "17:00",
  },
  {
    startTime: "09:00",
    endTime: "17:00",
  },
];
const result = incidentResolutionPerformance(
  new Date(startTime),
  new Date(endTime),
  businessHours
);
console.log("Effective time in ms: " + result);
console.log("Effective time in hr: " + result / 60 / 60 / 1000);

// 100800000
// 285000000 100800000
