package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IFilter;
import www.google.com.digitalbuildings._0_0_1.subfields.IAlarm;

public interface IFilter_alarm_status extends IField{

	public IRI iri();

    public void addComposedOfAlarm (IAlarm parameter);

	public Set<IAlarm> getComposedOfAlarm();

    public void addComposedOfFilter (IFilter parameter);

	public Set<IFilter> getComposedOfFilter();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}