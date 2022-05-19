// swift-tools-version: 5.6
import PackageDescription

let package = Package(
    name: "Marc",
    products: [
        .library(name: "Marc", targets: ["Marc"]),
    ],
    dependencies: [],
    targets: [
        .target(name: "Marc", dependencies: []),
        .testTarget(name: "MarcTests", dependencies: ["Marc"]),
    ]
)
