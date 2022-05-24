// swift-tools-version: 5.6
import PackageDescription

let package = Package(
    name: "Marc",
    products: [
        .library(name: "Marc", targets: ["Marc"])
    ],
    targets: [
        .target(name: "Marc", path: "swift/Sources"),
        .testTarget(name: "MarcTests", dependencies: ["Marc"], path: "swift/Tests")
    ]
)
