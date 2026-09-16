try {
    Write-Host "Acquiring Tokens..."
    $pbiToken = (Get-AzAccessToken -ResourceUrl "https://analysis.windows.net/powerbi/api").Token
    $fabricToken = (Get-AzAccessToken -ResourceUrl "https://api.fabric.microsoft.com").Token
    
    Write-Host "1. Testing Power BI API (https://api.powerbi.com/v1.0/myorg/groups)..."
    $headersPBI = @{ "Authorization" = "Bearer $pbiToken" }
    try {
        $pbiRes = Invoke-RestMethod -Uri "https://api.powerbi.com/v1.0/myorg/groups" -Headers $headersPBI -Method Get
        Write-Host "SUCCESS Power BI API! Found $($pbiRes.value.Count) workspaces:"
        foreach ($ws in $pbiRes.value) {
            Write-Host " - Workspace: $($ws.name) (ID: $($ws.id))"
        }
    } catch {
        Write-Host "Power BI API Failed: $_"
    }

    Write-Host "2. Testing Fabric API with PBI Token..."
    try {
        $fabRes1 = Invoke-RestMethod -Uri "https://api.fabric.microsoft.com/v1/workspaces" -Headers $headersPBI -Method Get
        Write-Host "SUCCESS Fabric API (using PBI Token)! Found $($fabRes1.value.Count) workspaces:"
        foreach ($ws in $fabRes1.value) {
            Write-Host " - Workspace: $($ws.displayName) (ID: $($ws.id))"
        }
    } catch {
        Write-Host "Fabric API (PBI Token) Failed: $_"
    }

    Write-Host "3. Testing Fabric API with Fabric Token..."
    $headersFab = @{ "Authorization" = "Bearer $fabricToken" }
    try {
        $fabRes2 = Invoke-RestMethod -Uri "https://api.fabric.microsoft.com/v1/workspaces" -Headers $headersFab -Method Get
        Write-Host "SUCCESS Fabric API (using Fabric Token)! Found $($fabRes2.value.Count) workspaces:"
        foreach ($ws in $fabRes2.value) {
            Write-Host " - Workspace: $($ws.displayName) (ID: $($ws.id))"
        }
    } catch {
        Write-Host "Fabric API (Fabric Token) Failed: $_"
    }

} catch {
    Write-Error $_
}
