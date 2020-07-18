package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IAlarm;
import www.google.com.digitalbuildings._0_0_1.subfields.IFabric;
import www.google.com.digitalbuildings._0_0_1.subfields.IProtection;

public interface IFabric_protection_alarm_status extends IField{

	public IRI iri();

    public void addComposedOfAlarm (IAlarm parameter);

	public Set<IAlarm> getComposedOfAlarm();

    public void addComposedOfFabric (IFabric parameter);

	public Set<IFabric> getComposedOfFabric();

    public void addComposedOfProtection (IProtection parameter);

	public Set<IProtection> getComposedOfProtection();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}