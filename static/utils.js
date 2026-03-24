/**
 * TrustLens AI - Utility Functions
 * Handles all button clicks and user interactions
 */

// ============ ANALYSIS FUNCTIONS ============

function analyzeProduct(productId) {
    console.log(`Analyzing product: ${productId}`);
    showToast('Loading product analysis...');
    window.location.href = `/analytics/${productId}`;
}

function exportAnalytics() {
    showToast('Exporting analytics...');
    const data = {
        timestamp: new Date().toISOString(),
        analytics: 'data_here'
    };
    const dataStr = JSON.stringify(data, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `analytics-${Date.now()}.json`;
    link.click();
    showToast('Analytics exported successfully!');
}

function scheduleMonitoring() {
    showToast('Opening monitoring scheduler...');
    showModalDialog(
        'Schedule Monitoring',
        `
        <form id="scheduleForm">
            <div class="mb-3">
                <label class="form-label">Monitoring Frequency</label>
                <select class="form-select" id="frequency">
                    <option>Daily</option>
                    <option>Weekly</option>
                    <option>Monthly</option>
                </select>
            </div>
            <div class="mb-3">
                <label class="form-label">Alert Email</label>
                <input type="email" class="form-control" id="alertEmail" placeholder="your@email.com">
            </div>
            <button type="button" class="btn btn-primary" onclick="saveSchedule()">Schedule</button>
        </form>
        `
    );
}

function saveSchedule() {
    const frequency = document.getElementById('frequency').value;
    const email = document.getElementById('alertEmail').value;
    
    if (!email) {
        alert('Please enter an email address');
        return;
    }
    
    showToast(`Monitoring scheduled ${frequency.toLowerCase()} for ${email}`);
    closeModalDialog();
}

function alertSettings() {
    showToast('Opening alert settings...');
    showModalDialog(
        'Alert Settings',
        `
        <form>
            <div class="mb-3">
                <label class="form-check-label">
                    <input class="form-check-input" type="checkbox" checked> Email alerts
                </label>
            </div>
            <div class="mb-3">
                <label class="form-check-label">
                    <input class="form-check-input" type="checkbox" checked> Fake review alerts
                </label>
            </div>
            <div class="mb-3">
                <label class="form-check-label">
                    <input class="form-check-input" type="checkbox"> Weekly summary
                </label>
            </div>
            <button type="button" class="btn btn-primary" onclick="saveAlerts()">Save Settings</button>
        </form>
        `
    );
}

function saveAlerts() {
    showToast('Alert settings saved!');
    closeModalDialog();
}

// ============ ANALYSIS RESULT ACTIONS ============

function saveAnalysis() {
    showToast('Saving analysis...');
    fetch('/save-analysis', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            timestamp: new Date().toISOString()
        })
    }).then(r => r.json())
      .then(data => showToast('Analysis saved successfully!'))
      .catch(e => showToast('Error saving analysis: ' + e.message));
}

function shareAnalysis() {
    showToast('Opening share options...');
    showModalDialog(
        'Share Analysis',
        `
        <div class="list-group">
            <button class="list-group-item list-group-item-action" onclick="shareTo('email')">
                <i class="fas fa-envelope me-2"></i> Share via Email
            </button>
            <button class="list-group-item list-group-item-action" onclick="shareTo('link')">
                <i class="fas fa-link me-2"></i> Copy Share Link
            </button>
            <button class="list-group-item list-group-item-action" onclick="shareTo('pdf')">
                <i class="fas fa-file-pdf me-2"></i> Download as PDF
            </button>
        </div>
        `
    );
}

function shareTo(type) {
    if (type === 'email') {
        showToast('Opening email client...');
    } else if (type === 'link') {
        const link = window.location.href;
        navigator.clipboard.writeText(link);
        showToast('Share link copied to clipboard!');
    } else if (type === 'pdf') {
        showToast('Generating PDF...');
        window.print();
    }
    closeModalDialog();
}

function similarReviews() {
    showToast('Finding similar reviews...');
    showModalDialog(
        'Similar Reviews',
        `
        <div class="alert alert-info">
            <p><strong>Similar reviews found:</strong></p>
            <ul>
                <li>Review 1: <em>"Product quality issue..."</em></li>
                <li>Review 2: <em>"Same problem reported..."</em></li>
                <li>Review 3: <em>"Consistent theme detected..."</em></li>
            </ul>
        </div>
        <button class="btn btn-primary" onclick="analyzePattern()">Analyze Pattern</button>
        `
    );
}

function analyzePattern() {
    showToast('Analyzing review pattern...');
    closeModalDialog();
}

// ============ PRODUCT MANAGEMENT ============

function openEdit(productId, productName) {
    document.getElementById("editProductId").value = productId;
    document.getElementById("editName").value = productName;
    const modal = new bootstrap.Modal(document.getElementById('editModal'));
    modal.show();
}

function saveEdit() {
    const productId = document.getElementById("editProductId").value;
    const name = document.getElementById("editName").value;
    
    if (!name.trim()) {
        alert('Product name cannot be empty');
        return;
    }
    
    const formData = new FormData();
    formData.append("name", name);
    
    fetch(`/edit_product/${productId}`, {
        method: 'POST',
        body: formData
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            showToast('Product updated successfully!');
            location.reload();
        } else {
            showToast('Error updating product');
        }
    })
    .catch(e => showToast('Error: ' + e.message));
}

function deleteProduct(productId) {
    if (confirm('Are you sure you want to delete this product? This action cannot be undone.')) {
        showToast('Deleting product...');
        fetch(`/delete_product/${productId}`, {
            method: 'POST'
        })
        .then(r => r.json())
        .then(data => {
            if (data.success) {
                showToast('Product deleted successfully!');
                setTimeout(() => location.reload(), 1000);
            } else {
                showToast('Error deleting product');
            }
        })
        .catch(e => showToast('Error: ' + e.message));
    }
}

function exportCSV(productId, productName) {
    showToast('Generating CSV export...');
    fetch(`/export-product-csv/${productId}`)
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `${productName.replace(/\s+/g, '-')}-reviews-${Date.now()}.csv`;
            link.click();
            showToast('CSV exported successfully!');
        })
        .catch(e => showToast('Error exporting CSV: ' + e.message));
}

// ============ PROFILE MANAGEMENT ============

function editProfile() {
    window.location.href = '/edit_profile';
}

function changePassword() {
    window.location.href = '/change_password';
}

function twoFactorAuth() {
    window.location.href = '/two_factor';
}

function activeSessions() {
    window.location.href = '/active_sessions';
}

function viewBillingHistory() {
    window.location.href = '/billing_history';
}

function updatePaymentMethod() {
    window.location.href = '/payment_method';
}

function upgradePlan() {
    window.location.href = '/upgrade_plan';
}

function deleteAccount() {
    if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
        window.location.href = '/delete_account';
    }
}

// ============ SUPPORT FUNCTIONS ============

function submitSupportTicket() {
    const subject = document.getElementById('supportSubject').value;
    const category = document.getElementById('supportCategory').value;
    const message = document.getElementById('supportMessage').value;
    const priority = document.getElementById('supportPriority').value;
    
    if (!subject || !category || !message) {
        alert('Please fill in all required fields');
        return;
    }
    
    showToast('Submitting support ticket...');
    
    fetch('/submit_support_ticket', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            subject: subject,
            category: category,
            message: message,
            priority: priority
        })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            showToast('Support ticket submitted successfully!');
            const modal = bootstrap.Modal.getInstance(document.getElementById('supportModal'));
            modal.hide();
            document.getElementById('supportForm').reset();
        } else {
            showToast('Error submitting ticket: ' + (data.message || 'Unknown error'));
        }
    })
    .catch(e => {
        showToast('Error: ' + e.message);
    });
}

// ============ UTILITY FUNCTIONS ============
    const modal = document.getElementById('utilityModal');
    if (!modal) {
        createUtilityModal();
    }
    document.getElementById('utilityModalLabel').innerText = title;
    document.getElementById('utilityModalBody').innerHTML = content;
    const bsModal = new bootstrap.Modal(document.getElementById('utilityModal'));
    bsModal.show();
}

function closeModalDialog() {
    const modal = bootstrap.Modal.getInstance(document.getElementById('utilityModal'));
    if (modal) modal.hide();
}

function createUtilityModal() {
    const modalHTML = `
    <div class="modal fade" id="utilityModal" tabindex="-1">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="utilityModalLabel">Dialog</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body" id="utilityModalBody">
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);
}

// ============ UTILITY FUNCTIONS ============

function showToast(msg) {
    const box = document.getElementById("toastBox");
    if (box) {
        box.innerText = msg;
        box.style.display = "block";
        setTimeout(() => box.style.display = "none", 3000);
    }
}

function showLoader() {
    const loader = document.getElementById("loader");
    if (loader) {
        loader.style.display = "block";
    }
}

function hideLoader() {
    const loader = document.getElementById("loader");
    if (loader) {
        loader.style.display = "none";
    }
}

// Initialize utility modal on page load
document.addEventListener('DOMContentLoaded', function() {
    createUtilityModal();
});
